from . import base_types
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text
from .UpdateType16Choice import UpdateType16Choice
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .YesNoIndicator import YesNoIndicator
from .Number3Choice import Number3Choice

class Statement68(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_RptNb", "_StmtDtTm", "_CtrPtyPrtflTrfNtfctnRef", "_UpdTp", "_StmtId"]
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
	def StmtDtTm(self):
		return self._StmtDtTm

	@StmtDtTm.setter
	def StmtDtTm(self, value):
		self._StmtDtTm = value if type(value) != base_types.auto else self.make_default("StmtDtTm")

	@StmtDtTm.deleter
	def StmtDtTm(self):
		del self._StmtDtTm
		self._StmtDtTm = None

	@property
	def CtrPtyPrtflTrfNtfctnRef(self):
		return self._CtrPtyPrtflTrfNtfctnRef

	@CtrPtyPrtflTrfNtfctnRef.setter
	def CtrPtyPrtflTrfNtfctnRef(self, value):
		self._CtrPtyPrtflTrfNtfctnRef = value if type(value) != base_types.auto else self.make_default("CtrPtyPrtflTrfNtfctnRef")

	@CtrPtyPrtflTrfNtfctnRef.deleter
	def CtrPtyPrtflTrfNtfctnRef(self):
		del self._CtrPtyPrtflTrfNtfctnRef
		self._CtrPtyPrtflTrfNtfctnRef = None

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

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if type(value) != base_types.auto else self.make_default("StmtId")

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyPrtflTrfNtfctnRef', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType16Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
	))

