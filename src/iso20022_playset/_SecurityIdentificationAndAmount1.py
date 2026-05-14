# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._ProductType7Code import ProductType7Code

class SecurityIdentificationAndAmount1(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmTp", "_Id", "_MktVal"]
	@property
	def FinInstrmTp(self):
		return self._FinInstrmTp

	@FinInstrmTp.setter
	def FinInstrmTp(self, value):
		self._FinInstrmTp = value if type(value) != base_types.auto else self.make_default("FinInstrmTp")

	@FinInstrmTp.deleter
	def FinInstrmTp(self):
		del self._FinInstrmTp
		self._FinInstrmTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != base_types.auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmTp', type=ProductType7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
	))