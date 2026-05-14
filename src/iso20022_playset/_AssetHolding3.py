# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from ._AssetHolding3Choice import AssetHolding3Choice
from ._CollateralAccountType3Code import CollateralAccountType3Code

class AssetHolding3(base_types._BaseFieldType):

	__slots__ = ["_AsstTp", "_CollRqrmnt", "_PstHrcutVal"]
	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if type(value) != base_types.auto else self.make_default("AsstTp")

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = None

	@property
	def CollRqrmnt(self):
		return self._CollRqrmnt

	@CollRqrmnt.setter
	def CollRqrmnt(self, value):
		self._CollRqrmnt = value if type(value) != base_types.auto else self.make_default("CollRqrmnt")

	@CollRqrmnt.deleter
	def CollRqrmnt(self):
		del self._CollRqrmnt
		self._CollRqrmnt = None

	@property
	def PstHrcutVal(self):
		return self._PstHrcutVal

	@PstHrcutVal.setter
	def PstHrcutVal(self, value):
		self._PstHrcutVal = value if type(value) != base_types.auto else self.make_default("PstHrcutVal")

	@PstHrcutVal.deleter
	def PstHrcutVal(self):
		del self._PstHrcutVal
		self._PstHrcutVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstTp', type=AssetHolding3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollRqrmnt', type=CollateralAccountType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstHrcutVal', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
	))