# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationReason39Choice
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6

class CancellationProcessingStatus10Choice(base_types._BaseFieldType):

	__slots__ = ["_CxlCmpltd", "_CxlPdg", "_CxlReqd", "_PrtrySts"]
	@property
	def CxlCmpltd(self):
		return self._CxlCmpltd

	@CxlCmpltd.setter
	def CxlCmpltd(self, value):
		self._CxlCmpltd = value if value is not None else base_types.UninitialisedField(self, 'CxlCmpltd', ProprietaryReason4, False)

	@CxlCmpltd.deleter
	def CxlCmpltd(self):
		del self._CxlCmpltd
		self._CxlCmpltd = base_types.UninitialisedField(self, 'CxlCmpltd', ProprietaryReason4, False)

	@property
	def CxlPdg(self):
		return self._CxlPdg

	@CxlPdg.setter
	def CxlPdg(self, value):
		self._CxlPdg = value if value is not None else base_types.UninitialisedField(self, 'CxlPdg', CancellationReason39Choice, False)

	@CxlPdg.deleter
	def CxlPdg(self):
		del self._CxlPdg
		self._CxlPdg = base_types.UninitialisedField(self, 'CxlPdg', CancellationReason39Choice, False)

	@property
	def CxlReqd(self):
		return self._CxlReqd

	@CxlReqd.setter
	def CxlReqd(self, value):
		self._CxlReqd = value if value is not None else base_types.UninitialisedField(self, 'CxlReqd', ProprietaryReason4, False)

	@CxlReqd.deleter
	def CxlReqd(self):
		del self._CxlReqd
		self._CxlReqd = base_types.UninitialisedField(self, 'CxlReqd', ProprietaryReason4, False)

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if value is not None else base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason6, False)

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlCmpltd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlPdg', type=CancellationReason39Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReqd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
	))