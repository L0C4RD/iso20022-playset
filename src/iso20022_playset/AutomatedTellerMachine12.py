import base_types
import PointOfInteractionCapabilities10
import ActiveCurrencyCode
import PostalAddress17
import TransactionEnvironment2Code
import ATMEquipment1
import Max35Text

class AutomatedTellerMachine12(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Lctn", "_BaseCcy", "_LctnCtgy", "_AddtlId", "_Cpblties", "_SeqNb", "_Eqpmnt"]
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
	def Cpblties(self):
		return self._Cpblties

	@Cpblties.setter
	def Cpblties(self, value):
		self._Cpblties = value if type(value) != auto else self.make_default("Cpblties")

	@Cpblties.deleter
	def Cpblties(self):
		del self._Cpblties
		self._Cpblties = None

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
	def Eqpmnt(self):
		return self._Eqpmnt

	@Eqpmnt.setter
	def Eqpmnt(self, value):
		self._Eqpmnt = value if type(value) != auto else self.make_default("Eqpmnt")

	@Eqpmnt.deleter
	def Eqpmnt(self):
		del self._Eqpmnt
		self._Eqpmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=PostalAddress17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnCtgy', type=TransactionEnvironment2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cpblties', type=PointOfInteractionCapabilities10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Eqpmnt', type=ATMEquipment1, min=0, max=1, mutex_group=None, array=False),
	))

