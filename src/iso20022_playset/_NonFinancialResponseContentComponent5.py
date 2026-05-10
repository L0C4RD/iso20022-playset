from . import base_types
from .Acquirer10 import Acquirer10
from .RecurringTransaction6 import RecurringTransaction6
from .NonFinancialRequestType2Code import NonFinancialRequestType2Code
from .ResponseType11 import ResponseType11
from .ExternallyDefinedData5 import ExternallyDefinedData5
from .NonFinancialResponseRisk1Code import NonFinancialResponseRisk1Code
from .Action17 import Action17

class NonFinancialResponseContentComponent5(base_types._BaseFieldType):

	__slots__ = ["_Instlmt", "_AcqrrSelctd", "_RskMgmtRslt", "_Actn", "_AddtlRspn", "_Rspn", "_NonFinReqTp"]
	@property
	def Instlmt(self):
		return self._Instlmt

	@Instlmt.setter
	def Instlmt(self, value):
		self._Instlmt = value if type(value) != base_types.auto else self.make_default("Instlmt")

	@Instlmt.deleter
	def Instlmt(self):
		del self._Instlmt
		self._Instlmt = None

	@property
	def AcqrrSelctd(self):
		return self._AcqrrSelctd

	@AcqrrSelctd.setter
	def AcqrrSelctd(self, value):
		self._AcqrrSelctd = value if type(value) != base_types.auto else self.make_default("AcqrrSelctd")

	@AcqrrSelctd.deleter
	def AcqrrSelctd(self):
		del self._AcqrrSelctd
		self._AcqrrSelctd = None

	@property
	def RskMgmtRslt(self):
		return self._RskMgmtRslt

	@RskMgmtRslt.setter
	def RskMgmtRslt(self, value):
		self._RskMgmtRslt = value if type(value) != base_types.auto else self.make_default("RskMgmtRslt")

	@RskMgmtRslt.deleter
	def RskMgmtRslt(self):
		del self._RskMgmtRslt
		self._RskMgmtRslt = None

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != base_types.auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def AddtlRspn(self):
		return self._AddtlRspn

	@AddtlRspn.setter
	def AddtlRspn(self, value):
		self._AddtlRspn = value if type(value) != base_types.auto else self.make_default("AddtlRspn")

	@AddtlRspn.deleter
	def AddtlRspn(self):
		del self._AddtlRspn
		self._AddtlRspn = None

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != base_types.auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def NonFinReqTp(self):
		return self._NonFinReqTp

	@NonFinReqTp.setter
	def NonFinReqTp(self, value):
		self._NonFinReqTp = value if type(value) != base_types.auto else self.make_default("NonFinReqTp")

	@NonFinReqTp.deleter
	def NonFinReqTp(self):
		del self._NonFinReqTp
		self._NonFinReqTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Instlmt', type=RecurringTransaction6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcqrrSelctd', type=Acquirer10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskMgmtRslt', type=NonFinancialResponseRisk1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actn', type=Action17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlRspn', type=ExternallyDefinedData5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonFinReqTp', type=NonFinancialRequestType2Code, min=1, max=1, mutex_group=None, array=False),
	))

