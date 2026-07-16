# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CollateralType1Code

class Collateral6(base_types._BaseFieldType):

	__slots__ = ["_CollTp", "_MktVal", "_PstHrcutVal"]
	@property
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if value is not None else base_types.UninitialisedField(self, 'CollTp', CollateralType1Code, False)

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = base_types.UninitialisedField(self, 'CollTp', CollateralType1Code, False)

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', ActiveCurrencyAndAmount, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', ActiveCurrencyAndAmount, False)

	@property
	def PstHrcutVal(self):
		return self._PstHrcutVal

	@PstHrcutVal.setter
	def PstHrcutVal(self, value):
		self._PstHrcutVal = value if value is not None else base_types.UninitialisedField(self, 'PstHrcutVal', ActiveCurrencyAndAmount, False)

	@PstHrcutVal.deleter
	def PstHrcutVal(self):
		del self._PstHrcutVal
		self._PstHrcutVal = base_types.UninitialisedField(self, 'PstHrcutVal', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollTp', type=CollateralType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstHrcutVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))