from . import base_types
from .Document9 import Document9
from .Demand2 import Demand2
from .Max2000Text import Max2000Text
from .ISODate import ISODate
from .Contacts3 import Contacts3
from .Undertaking9 import Undertaking9
from .BankInstructions1 import BankInstructions1

class ExtendOrPayQuery1(base_types._BaseFieldType):

	__slots__ = ["_DmndDtls", "_NclsdFile", "_BkCtct", "_BkInstrs", "_ReqdXpryDt", "_UdrtkgId", "_AddtlInf"]
	@property
	def DmndDtls(self):
		return self._DmndDtls

	@DmndDtls.setter
	def DmndDtls(self, value):
		self._DmndDtls = value if type(value) != base_types.auto else self.make_default("DmndDtls")

	@DmndDtls.deleter
	def DmndDtls(self):
		del self._DmndDtls
		self._DmndDtls = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != base_types.auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def BkCtct(self):
		return self._BkCtct

	@BkCtct.setter
	def BkCtct(self, value):
		self._BkCtct = value if type(value) != base_types.auto else self.make_default("BkCtct")

	@BkCtct.deleter
	def BkCtct(self):
		del self._BkCtct
		self._BkCtct = None

	@property
	def BkInstrs(self):
		return self._BkInstrs

	@BkInstrs.setter
	def BkInstrs(self, value):
		self._BkInstrs = value if type(value) != base_types.auto else self.make_default("BkInstrs")

	@BkInstrs.deleter
	def BkInstrs(self):
		del self._BkInstrs
		self._BkInstrs = None

	@property
	def ReqdXpryDt(self):
		return self._ReqdXpryDt

	@ReqdXpryDt.setter
	def ReqdXpryDt(self, value):
		self._ReqdXpryDt = value if type(value) != base_types.auto else self.make_default("ReqdXpryDt")

	@ReqdXpryDt.deleter
	def ReqdXpryDt(self):
		del self._ReqdXpryDt
		self._ReqdXpryDt = None

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != base_types.auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DmndDtls', type=Demand2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkCtct', type=Contacts3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkInstrs', type=BankInstructions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdXpryDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

