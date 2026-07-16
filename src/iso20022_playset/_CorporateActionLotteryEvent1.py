# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LotteryFeatureType1Code
from . import LotteryTypeFormat4Choice

class CorporateActionLotteryEvent1(base_types._BaseFieldType):

	__slots__ = ["_FeatrTp", "_Tp"]
	@property
	def FeatrTp(self):
		return self._FeatrTp

	@FeatrTp.setter
	def FeatrTp(self, value):
		self._FeatrTp = value if value is not None else base_types.UninitialisedField(self, 'FeatrTp', LotteryFeatureType1Code, False)

	@FeatrTp.deleter
	def FeatrTp(self):
		del self._FeatrTp
		self._FeatrTp = base_types.UninitialisedField(self, 'FeatrTp', LotteryFeatureType1Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', LotteryTypeFormat4Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', LotteryTypeFormat4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FeatrTp', type=LotteryFeatureType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=LotteryTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))