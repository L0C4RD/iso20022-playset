from . import base_types
from ._Number3Choice import Number3Choice
from ._YesNoIndicator import YesNoIndicator
from ._Max35Text import Max35Text
from ._Period7Choice import Period7Choice
from ._UpdateType15Choice import UpdateType15Choice
from ._Frequency22Choice import Frequency22Choice
from ._DateAndDateTime2Choice import DateAndDateTime2Choice

class IntraBalanceReport6(base_types._BaseFieldType):

	__slots__ = ["_Frqcy", "_RptNb", "_RptPrd", "_ActvtyInd", "_QryRef", "_RptId", "_UpdTp", "_RptDtTm"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != base_types.auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if type(value) != base_types.auto else self.make_default("QryRef")

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = None

	@property
	def RptDtTm(self):
		return self._RptDtTm

	@RptDtTm.setter
	def RptDtTm(self, value):
		self._RptDtTm = value if type(value) != base_types.auto else self.make_default("RptDtTm")

	@RptDtTm.deleter
	def RptDtTm(self):
		del self._RptDtTm
		self._RptDtTm = None

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != base_types.auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if type(value) != base_types.auto else self.make_default("RptNb")

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = None

	@property
	def RptPrd(self):
		return self._RptPrd

	@RptPrd.setter
	def RptPrd(self, value):
		self._RptPrd = value if type(value) != base_types.auto else self.make_default("RptPrd")

	@RptPrd.deleter
	def RptPrd(self):
		del self._RptPrd
		self._RptPrd = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != base_types.auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency22Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPrd', type=Period7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=1, max=1, mutex_group=None, array=False),
	))

