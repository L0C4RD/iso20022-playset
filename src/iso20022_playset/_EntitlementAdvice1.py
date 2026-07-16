# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionOption1FormatChoice
from . import DateFormat4Choice
from . import Entitlement1
from . import Exact3NumericText

class EntitlementAdvice1(base_types._BaseFieldType):

	__slots__ = ["_AcctAndDstrbtnDtls", "_OptnNb", "_OptnTp", "_PmtDt", "_RcrdDt"]
	@property
	def AcctAndDstrbtnDtls(self):
		return self._AcctAndDstrbtnDtls

	@AcctAndDstrbtnDtls.setter
	def AcctAndDstrbtnDtls(self, value):
		self._AcctAndDstrbtnDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctAndDstrbtnDtls', Entitlement1, True)

	@AcctAndDstrbtnDtls.deleter
	def AcctAndDstrbtnDtls(self):
		del self._AcctAndDstrbtnDtls
		self._AcctAndDstrbtnDtls = base_types.UninitialisedField(self, 'AcctAndDstrbtnDtls', Entitlement1, True)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDt', DateFormat4Choice, False)

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = base_types.UninitialisedField(self, 'PmtDt', DateFormat4Choice, False)

	@property
	def RcrdDt(self):
		return self._RcrdDt

	@RcrdDt.setter
	def RcrdDt(self, value):
		self._RcrdDt = value if value is not None else base_types.UninitialisedField(self, 'RcrdDt', DateFormat4Choice, False)

	@RcrdDt.deleter
	def RcrdDt(self):
		del self._RcrdDt
		self._RcrdDt = base_types.UninitialisedField(self, 'RcrdDt', DateFormat4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctAndDstrbtnDtls', type=Entitlement1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDt', type=DateFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))