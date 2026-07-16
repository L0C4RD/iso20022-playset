# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max5NumericText

class AddressVerification1(base_types._BaseFieldType):

	__slots__ = ["_AdrDgts", "_PstlCdDgts"]
	@property
	def AdrDgts(self):
		return self._AdrDgts

	@AdrDgts.setter
	def AdrDgts(self, value):
		self._AdrDgts = value if value is not None else base_types.UninitialisedField(self, 'AdrDgts', Max5NumericText, False)

	@AdrDgts.deleter
	def AdrDgts(self):
		del self._AdrDgts
		self._AdrDgts = base_types.UninitialisedField(self, 'AdrDgts', Max5NumericText, False)

	@property
	def PstlCdDgts(self):
		return self._PstlCdDgts

	@PstlCdDgts.setter
	def PstlCdDgts(self, value):
		self._PstlCdDgts = value if value is not None else base_types.UninitialisedField(self, 'PstlCdDgts', Max5NumericText, False)

	@PstlCdDgts.deleter
	def PstlCdDgts(self):
		del self._PstlCdDgts
		self._PstlCdDgts = base_types.UninitialisedField(self, 'PstlCdDgts', Max5NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrDgts', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlCdDgts', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
	))