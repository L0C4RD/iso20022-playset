from . import base_types
from .CorporateActionOption1FormatChoice import CorporateActionOption1FormatChoice
from .Exact3NumericText import Exact3NumericText
from .Entitlement1 import Entitlement1
from .DateFormat4Choice import DateFormat4Choice

class EntitlementAdvice1(base_types._BaseFieldType):

	__slots__ = ["_RcrdDt", "_AcctAndDstrbtnDtls", "_OptnNb", "_OptnTp", "_PmtDt"]
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

	@property
	def AcctAndDstrbtnDtls(self):
		return self._AcctAndDstrbtnDtls

	@AcctAndDstrbtnDtls.setter
	def AcctAndDstrbtnDtls(self, value):
		self._AcctAndDstrbtnDtls = value if type(value) != base_types.auto else self.make_default("AcctAndDstrbtnDtls")

	@AcctAndDstrbtnDtls.deleter
	def AcctAndDstrbtnDtls(self):
		del self._AcctAndDstrbtnDtls
		self._AcctAndDstrbtnDtls = None

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
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if type(value) != base_types.auto else self.make_default("PmtDt")

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcrdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctAndDstrbtnDtls', type=Entitlement1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))

