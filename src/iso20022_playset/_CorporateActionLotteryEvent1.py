# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LotteryFeatureType1Code import LotteryFeatureType1Code
from ._LotteryTypeFormat4Choice import LotteryTypeFormat4Choice

class CorporateActionLotteryEvent1(base_types._BaseFieldType):

	__slots__ = ["_FeatrTp", "_Tp"]
	@property
	def FeatrTp(self):
		return self._FeatrTp

	@FeatrTp.setter
	def FeatrTp(self, value):
		self._FeatrTp = value if type(value) != base_types.auto else self.make_default("FeatrTp")

	@FeatrTp.deleter
	def FeatrTp(self):
		del self._FeatrTp
		self._FeatrTp = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FeatrTp', type=LotteryFeatureType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=LotteryTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))