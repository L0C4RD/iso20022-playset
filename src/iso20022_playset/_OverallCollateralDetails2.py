# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralAmount15
from . import CollateralStatus1Code
from . import DateAndDateTime2Choice
from . import Max350Text
from . import PercentageRate

class OverallCollateralDetails2(base_types._BaseFieldType):

	__slots__ = ["_CollAddtlDtls", "_GblCollSts", "_MrgnRate", "_ValtnAmts", "_ValtnDt"]
	@property
	def CollAddtlDtls(self):
		return self._CollAddtlDtls

	@CollAddtlDtls.setter
	def CollAddtlDtls(self, value):
		self._CollAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'CollAddtlDtls', Max350Text, False)

	@CollAddtlDtls.deleter
	def CollAddtlDtls(self):
		del self._CollAddtlDtls
		self._CollAddtlDtls = base_types.UninitialisedField(self, 'CollAddtlDtls', Max350Text, False)

	@property
	def GblCollSts(self):
		return self._GblCollSts

	@GblCollSts.setter
	def GblCollSts(self, value):
		self._GblCollSts = value if value is not None else base_types.UninitialisedField(self, 'GblCollSts', CollateralStatus1Code, False)

	@GblCollSts.deleter
	def GblCollSts(self):
		del self._GblCollSts
		self._GblCollSts = base_types.UninitialisedField(self, 'GblCollSts', CollateralStatus1Code, False)

	@property
	def MrgnRate(self):
		return self._MrgnRate

	@MrgnRate.setter
	def MrgnRate(self, value):
		self._MrgnRate = value if value is not None else base_types.UninitialisedField(self, 'MrgnRate', PercentageRate, False)

	@MrgnRate.deleter
	def MrgnRate(self):
		del self._MrgnRate
		self._MrgnRate = base_types.UninitialisedField(self, 'MrgnRate', PercentageRate, False)

	@property
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if value is not None else base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount15, False)

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount15, False)

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if value is not None else base_types.UninitialisedField(self, 'ValtnDt', DateAndDateTime2Choice, False)

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = base_types.UninitialisedField(self, 'ValtnDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblCollSts', type=CollateralStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))