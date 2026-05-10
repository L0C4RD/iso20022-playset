from . import base_types
from .DateFormat4Choice import DateFormat4Choice
from .YesNoIndicator import YesNoIndicator
from .CorporateActionOption1FormatChoice import CorporateActionOption1FormatChoice
from .CashMovement1 import CashMovement1
from .Exact3NumericText import Exact3NumericText
from .SecurityMovement1 import SecurityMovement1

class GlobalDistributionRequest1(base_types._BaseFieldType):

	__slots__ = ["_PmtDt", "_SctiesMvmnt", "_PradvcInd", "_OptnNb", "_CshMvmnt", "_OptnTp", "_RcrdDt"]
	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if type(value) != base_types.auto else self.make_default("PmtDt")

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = None

	@property
	def SctiesMvmnt(self):
		return self._SctiesMvmnt

	@SctiesMvmnt.setter
	def SctiesMvmnt(self, value):
		self._SctiesMvmnt = value if type(value) != base_types.auto else self.make_default("SctiesMvmnt")

	@SctiesMvmnt.deleter
	def SctiesMvmnt(self):
		del self._SctiesMvmnt
		self._SctiesMvmnt = None

	@property
	def PradvcInd(self):
		return self._PradvcInd

	@PradvcInd.setter
	def PradvcInd(self, value):
		self._PradvcInd = value if type(value) != base_types.auto else self.make_default("PradvcInd")

	@PradvcInd.deleter
	def PradvcInd(self):
		del self._PradvcInd
		self._PradvcInd = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != base_types.auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def CshMvmnt(self):
		return self._CshMvmnt

	@CshMvmnt.setter
	def CshMvmnt(self, value):
		self._CshMvmnt = value if type(value) != base_types.auto else self.make_default("CshMvmnt")

	@CshMvmnt.deleter
	def CshMvmnt(self):
		del self._CshMvmnt
		self._CshMvmnt = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if type(value) != base_types.auto else self.make_default("RcrdDt")

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtDt', type=DateFormat4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmnt', type=SecurityMovement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PradvcInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CashMovement1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDt', type=DateFormat4Choice, min=1, max=1, mutex_group=None, array=False),
	))

