# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat42Choice
from . import Max35Text

class Series1(base_types._BaseFieldType):

	__slots__ = ["_SrsDt", "_SrsNm"]
	@property
	def SrsDt(self):
		return self._SrsDt

	@SrsDt.setter
	def SrsDt(self, value):
		self._SrsDt = value if value is not None else base_types.UninitialisedField(self, 'SrsDt', DateFormat42Choice, False)

	@SrsDt.deleter
	def SrsDt(self):
		del self._SrsDt
		self._SrsDt = base_types.UninitialisedField(self, 'SrsDt', DateFormat42Choice, False)

	@property
	def SrsNm(self):
		return self._SrsNm

	@SrsNm.setter
	def SrsNm(self, value):
		self._SrsNm = value if value is not None else base_types.UninitialisedField(self, 'SrsNm', Max35Text, False)

	@SrsNm.deleter
	def SrsNm(self):
		del self._SrsNm
		self._SrsNm = base_types.UninitialisedField(self, 'SrsNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SrsDt', type=DateFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrsNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))