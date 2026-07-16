# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference10

class References68Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrRef", "_PrvsRef"]
	@property
	def OthrRef(self):
		return self._OthrRef

	@OthrRef.setter
	def OthrRef(self, value):
		self._OthrRef = value if value is not None else base_types.UninitialisedField(self, 'OthrRef', AdditionalReference10, False)

	@OthrRef.deleter
	def OthrRef(self):
		del self._OthrRef
		self._OthrRef = base_types.UninitialisedField(self, 'OthrRef', AdditionalReference10, False)

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference10, False)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrRef', type=AdditionalReference10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=1, mutex_group=1, array=False),
	))