# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINXMax24Text
from . import RestrictedFINXMax8Text

class RateName2(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_RateNm"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', RestrictedFINXMax8Text, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', RestrictedFINXMax8Text, False)

	@property
	def RateNm(self):
		return self._RateNm

	@RateNm.setter
	def RateNm(self, value):
		self._RateNm = value if value is not None else base_types.UninitialisedField(self, 'RateNm', RestrictedFINXMax24Text, False)

	@RateNm.deleter
	def RateNm(self):
		del self._RateNm
		self._RateNm = base_types.UninitialisedField(self, 'RateNm', RestrictedFINXMax24Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=RestrictedFINXMax8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateNm', type=RestrictedFINXMax24Text, min=1, max=1, mutex_group=None, array=False),
	))