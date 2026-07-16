# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import Status27Choice

class StatusAndSubStatus2(base_types._BaseFieldType):

	__slots__ = ["_StsCd", "_SubStsCd"]
	@property
	def StsCd(self):
		return self._StsCd

	@StsCd.setter
	def StsCd(self, value):
		self._StsCd = value if value is not None else base_types.UninitialisedField(self, 'StsCd', Status27Choice, False)

	@StsCd.deleter
	def StsCd(self):
		del self._StsCd
		self._StsCd = base_types.UninitialisedField(self, 'StsCd', Status27Choice, False)

	@property
	def SubStsCd(self):
		return self._SubStsCd

	@SubStsCd.setter
	def SubStsCd(self, value):
		self._SubStsCd = value if value is not None else base_types.UninitialisedField(self, 'SubStsCd', Exact4AlphaNumericText, False)

	@SubStsCd.deleter
	def SubStsCd(self):
		del self._SubStsCd
		self._SubStsCd = base_types.UninitialisedField(self, 'SubStsCd', Exact4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsCd', type=Status27Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubStsCd', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))