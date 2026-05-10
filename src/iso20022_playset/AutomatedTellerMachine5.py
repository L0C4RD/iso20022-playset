from . import base_types
import ATMDevice2Code
import ATMEquipment1
import MessageProtection1Code
import TransactionEnvironment2Code
import Max35Text
import PostalAddress17
import ActiveCurrencyCode

class AutomatedTellerMachine5(base_types._BaseFieldType):

	__slots__ = ["_AddtlId", "_Lctn", "_Eqpmnt", "_BaseCcy", "_LctnCtgy", "_Id", "_OutOfSvcDvc", "_SeqNb", "_MsgPrtcn"]
	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if type(value) != auto else self.make_default("AddtlId")

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = None

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	@property
	def Eqpmnt(self):
		return self._Eqpmnt

	@Eqpmnt.setter
	def Eqpmnt(self, value):
		self._Eqpmnt = value if type(value) != auto else self.make_default("Eqpmnt")

	@Eqpmnt.deleter
	def Eqpmnt(self):
		del self._Eqpmnt
		self._Eqpmnt = None

	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if type(value) != auto else self.make_default("BaseCcy")

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = None

	@property
	def LctnCtgy(self):
		return self._LctnCtgy

	@LctnCtgy.setter
	def LctnCtgy(self, value):
		self._LctnCtgy = value if type(value) != auto else self.make_default("LctnCtgy")

	@LctnCtgy.deleter
	def LctnCtgy(self):
		del self._LctnCtgy
		self._LctnCtgy = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def OutOfSvcDvc(self):
		return self._OutOfSvcDvc

	@OutOfSvcDvc.setter
	def OutOfSvcDvc(self, value):
		self._OutOfSvcDvc = value if type(value) != auto else self.make_default("OutOfSvcDvc")

	@OutOfSvcDvc.deleter
	def OutOfSvcDvc(self):
		del self._OutOfSvcDvc
		self._OutOfSvcDvc = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def MsgPrtcn(self):
		return self._MsgPrtcn

	@MsgPrtcn.setter
	def MsgPrtcn(self, value):
		self._MsgPrtcn = value if type(value) != auto else self.make_default("MsgPrtcn")

	@MsgPrtcn.deleter
	def MsgPrtcn(self):
		del self._MsgPrtcn
		self._MsgPrtcn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=PostalAddress17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Eqpmnt', type=ATMEquipment1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnCtgy', type=TransactionEnvironment2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutOfSvcDvc', type=ATMDevice2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SeqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPrtcn', type=MessageProtection1Code, min=0, max=1, mutex_group=None, array=False),
	))

