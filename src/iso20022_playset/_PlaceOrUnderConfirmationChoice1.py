# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PlaceOfPresentation1
from . import PresentationParty1Code

class PlaceOrUnderConfirmationChoice1(base_types._BaseFieldType):

	__slots__ = ["_PlcOfPresntn", "_PresntnUdrConf"]
	@property
	def PlcOfPresntn(self):
		return self._PlcOfPresntn

	@PlcOfPresntn.setter
	def PlcOfPresntn(self, value):
		self._PlcOfPresntn = value if value is not None else base_types.UninitialisedField(self, 'PlcOfPresntn', PlaceOfPresentation1, False)

	@PlcOfPresntn.deleter
	def PlcOfPresntn(self):
		del self._PlcOfPresntn
		self._PlcOfPresntn = base_types.UninitialisedField(self, 'PlcOfPresntn', PlaceOfPresentation1, False)

	@property
	def PresntnUdrConf(self):
		return self._PresntnUdrConf

	@PresntnUdrConf.setter
	def PresntnUdrConf(self, value):
		self._PresntnUdrConf = value if value is not None else base_types.UninitialisedField(self, 'PresntnUdrConf', PresentationParty1Code, False)

	@PresntnUdrConf.deleter
	def PresntnUdrConf(self):
		del self._PresntnUdrConf
		self._PresntnUdrConf = base_types.UninitialisedField(self, 'PresntnUdrConf', PresentationParty1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlcOfPresntn', type=PlaceOfPresentation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PresntnUdrConf', type=PresentationParty1Code, min=0, max=1, mutex_group=1, array=False),
	))