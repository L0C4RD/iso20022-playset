# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd24Amount
from . import AssetHolding3Choice
from . import CollateralAccountType3Code

class AssetHolding3(base_types._BaseFieldType):

	__slots__ = ["_AsstTp", "_CollRqrmnt", "_PstHrcutVal"]
	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if value is not None else base_types.UninitialisedField(self, 'AsstTp', AssetHolding3Choice, False)

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = base_types.UninitialisedField(self, 'AsstTp', AssetHolding3Choice, False)

	@property
	def CollRqrmnt(self):
		return self._CollRqrmnt

	@CollRqrmnt.setter
	def CollRqrmnt(self, value):
		self._CollRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'CollRqrmnt', CollateralAccountType3Code, False)

	@CollRqrmnt.deleter
	def CollRqrmnt(self):
		del self._CollRqrmnt
		self._CollRqrmnt = base_types.UninitialisedField(self, 'CollRqrmnt', CollateralAccountType3Code, False)

	@property
	def PstHrcutVal(self):
		return self._PstHrcutVal

	@PstHrcutVal.setter
	def PstHrcutVal(self, value):
		self._PstHrcutVal = value if value is not None else base_types.UninitialisedField(self, 'PstHrcutVal', ActiveCurrencyAnd24Amount, False)

	@PstHrcutVal.deleter
	def PstHrcutVal(self):
		del self._PstHrcutVal
		self._PstHrcutVal = base_types.UninitialisedField(self, 'PstHrcutVal', ActiveCurrencyAnd24Amount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstTp', type=AssetHolding3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollRqrmnt', type=CollateralAccountType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstHrcutVal', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
	))