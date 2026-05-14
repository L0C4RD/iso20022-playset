# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._CorporateActionOption47Choice import CorporateActionOption47Choice
from ._CorporateActionPrice99 import CorporateActionPrice99
from ._Exact3NumericText import Exact3NumericText
from ._SecurityIdentification19 import SecurityIdentification19

class CorporateActionElection4(base_types._BaseFieldType):

	__slots__ = ["_CcyOptn", "_FinInstrmId", "_OptnNb", "_OptnTp", "_PricDtls"]
	@property
	def CcyOptn(self):
		return self._CcyOptn

	@CcyOptn.setter
	def CcyOptn(self, value):
		self._CcyOptn = value if type(value) != base_types.auto else self.make_default("CcyOptn")

	@CcyOptn.deleter
	def CcyOptn(self):
		del self._CcyOptn
		self._CcyOptn = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

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
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption47Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice99, min=0, max=1, mutex_group=None, array=False),
	))