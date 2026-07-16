# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MatchingReason5Choice
from . import MatchingReason6Choice
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6

class MatchingStatus35Choice(base_types._BaseFieldType):

	__slots__ = ["_Mtchd", "_MtchdWthTlrnce", "_MtchgAllgd", "_PrtrySts", "_Umtchd"]
	@property
	def Mtchd(self):
		return self._Mtchd

	@Mtchd.setter
	def Mtchd(self, value):
		self._Mtchd = value if value is not None else base_types.UninitialisedField(self, 'Mtchd', ProprietaryReason4, False)

	@Mtchd.deleter
	def Mtchd(self):
		del self._Mtchd
		self._Mtchd = base_types.UninitialisedField(self, 'Mtchd', ProprietaryReason4, False)

	@property
	def MtchdWthTlrnce(self):
		return self._MtchdWthTlrnce

	@MtchdWthTlrnce.setter
	def MtchdWthTlrnce(self, value):
		self._MtchdWthTlrnce = value if value is not None else base_types.UninitialisedField(self, 'MtchdWthTlrnce', ProprietaryReason4, False)

	@MtchdWthTlrnce.deleter
	def MtchdWthTlrnce(self):
		del self._MtchdWthTlrnce
		self._MtchdWthTlrnce = base_types.UninitialisedField(self, 'MtchdWthTlrnce', ProprietaryReason4, False)

	@property
	def MtchgAllgd(self):
		return self._MtchgAllgd

	@MtchgAllgd.setter
	def MtchgAllgd(self, value):
		self._MtchgAllgd = value if value is not None else base_types.UninitialisedField(self, 'MtchgAllgd', MatchingReason5Choice, False)

	@MtchgAllgd.deleter
	def MtchgAllgd(self):
		del self._MtchgAllgd
		self._MtchgAllgd = base_types.UninitialisedField(self, 'MtchgAllgd', MatchingReason5Choice, False)

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

	@property
	def Umtchd(self):
		return self._Umtchd

	@Umtchd.setter
	def Umtchd(self, value):
		self._Umtchd = value if value is not None else base_types.UninitialisedField(self, 'Umtchd', MatchingReason6Choice, False)

	@Umtchd.deleter
	def Umtchd(self):
		del self._Umtchd
		self._Umtchd = base_types.UninitialisedField(self, 'Umtchd', MatchingReason6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mtchd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtchdWthTlrnce', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtchgAllgd', type=MatchingReason5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Umtchd', type=MatchingReason6Choice, min=0, max=1, mutex_group=1, array=False),
	))