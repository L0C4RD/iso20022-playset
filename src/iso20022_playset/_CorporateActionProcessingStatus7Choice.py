# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionProcessingStatus5Choice
from . import YesNoIndicator

class CorporateActionProcessingStatus7Choice(base_types._BaseFieldType):

	__slots__ = ["_EvtInfSts", "_ForInfOnly"]
	@property
	def EvtInfSts(self):
		return self._EvtInfSts

	@EvtInfSts.setter
	def EvtInfSts(self, value):
		self._EvtInfSts = value if value is not None else base_types.UninitialisedField(self, 'EvtInfSts', CorporateActionProcessingStatus5Choice, False)

	@EvtInfSts.deleter
	def EvtInfSts(self):
		del self._EvtInfSts
		self._EvtInfSts = base_types.UninitialisedField(self, 'EvtInfSts', CorporateActionProcessingStatus5Choice, False)

	@property
	def ForInfOnly(self):
		return self._ForInfOnly

	@ForInfOnly.setter
	def ForInfOnly(self, value):
		self._ForInfOnly = value if value is not None else base_types.UninitialisedField(self, 'ForInfOnly', YesNoIndicator, False)

	@ForInfOnly.deleter
	def ForInfOnly(self):
		del self._ForInfOnly
		self._ForInfOnly = base_types.UninitialisedField(self, 'ForInfOnly', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtInfSts', type=CorporateActionProcessingStatus5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ForInfOnly', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))