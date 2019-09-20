import sqlite3 as dbimport timefrom LAMARCK_ML.individuals import IndividualInterfacefrom LAMARCK_ML.models.models import GenerationalModelfrom LAMARCK_ML.reproduction import AncestryEntityfrom LAMARCK_ML.reproduction.Ancestry_pb2 import AncestryProtofrom LAMARCK_ML.utils.dataSaver.dbConnection import DBConstantsfrom LAMARCK_ML.utils.dataSaver.interface import DataSaverInterfaceclass DSSqlite3(DataSaverInterface):  arg_FILE = 'file'  def __init__(self, **kwargs):    super(DSSqlite3, self).__init__(**kwargs)    self._file = kwargs.get(self.arg_FILE, 'default.db3')    self.conn = db.connect(self._file)    self.setup_db()  def setup_db(self):    cursor = self.conn.cursor()    cursor.execute(      "CREATE TABLE IF NOT EXISTS {} (rowid INTEGER PRIMARY KEY autoincrement, real_timestamp INTEGER, "      "abstract_timestamp INTEGER, id_name TEXT, serialized BLOB);".format(        DBConstants.table_individual.value[0]))    cursor.execute(      "CREATE TABLE IF NOT EXISTS {} (rowid INTEGER PRIMARY KEY autoincrement, real_timestamp INTEGER, "      "abstract_timestamp INTEGER, operation VARCHAR(8), descendant TEXT, serialized BLOB)".format(        DBConstants.table_ancestry.value[0]))    self.conn.commit()    cursor.close()  def get_individual_by_name(self, name):    cursor = self.conn.cursor()    cursor.execute("SELECT serialized FROM {} WHERE id_name=?".format(DBConstants.table_individual.value[0]), [name])    fetched = cursor.fetchone()    last = None    while fetched:      last = fetched[0]      fetched = cursor.fetchone()    cursor.close()    ind = IndividualInterface.__new__(IndividualInterface)    ind.__setstate__(last)    return ind  def end_evaluate(self, func):    def end_evaluate_wrapper(model: GenerationalModel):      cursor = self.conn.cursor()      real_timestamp = int(time.time())      abstract_timestampe = model.abstract_timestamp      for individual in model.generation:        statement = "INSERT INTO {} (real_timestamp, abstract_timestamp, id_name, serialized) " \                    "VALUES (?, ?, ?, ?);".format(          DBConstants.table_individual.value[0])        cursor.execute(statement, [real_timestamp,                                   abstract_timestampe,                                   individual.id_name,                                   db.Binary(individual.__getstate__())])      self.conn.commit()      cursor.close()      func()    return end_evaluate_wrapper  def end_reproduction_step(self, func):    def end_reproduction_step_wrapper(model):      cursor = self.conn.cursor()      real_timestamp = int(time.time())      abstract_timestamp = model.abstract_timestamp      _, ancestry = model.reproduction[-1]      statement = "INSERT INTO {} (real_timestamp, abstract_timestamp, operation, descendant, serialized) " \                  "VALUES (?, ?, ?, ?, ?);".format(        DBConstants.table_ancestry.value[0])      for anc in ancestry:        pb = anc.get_pb()        cursor.execute(statement, [real_timestamp,                                   abstract_timestamp,                                   pb.method,                                   pb.descendant,                                   db.Binary(pb.SerializeToString())])      self.conn.commit()      cursor.close()      func()    return end_reproduction_step_wrapper  def get_ancestry_for_ind(self, ind_name):    cursor = self.conn.cursor()    cursor.execute("SELECT serialized FROM {} WHERE descendant=?".format(      DBConstants.table_ancestry.value[0]), [ind_name])    fetched = cursor.fetchone()    last = None    while fetched:      last = fetched[0]      fetched = cursor.fetchone()    cursor.close()    if last is None:      return None    pb = AncestryProto()    pb.ParseFromString(last)    return AncestryEntity.from_pb(pb)