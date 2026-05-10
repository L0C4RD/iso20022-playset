import base_types
import ProprietaryStatusAndReason6
import ProprietaryReason4
import MatchingReason6Choice
import MatchingReason5Choice

class MatchingStatus35Choice(base_types._BaseFieldType):

	__slots__ = ["_MtchdWthTlrnce", "_PrtrySts", "_Umtchd", "_Mtchd", "_MtchgAllgd"]
	@property
	def MtchdWthTlrnce(self):
		return self._MtchdWthTlrnce

	@MtchdWthTlrnce.setter
	def MtchdWthTlrnce(self, value):
		self._MtchdWthTlrnce = value if type(value) != auto else self.make_default("MtchdWthTlrnce")

	@MtchdWthTlrnce.deleter
	def MtchdWthTlrnce(self):
		del self._MtchdWthTlrnce
		self._MtchdWthTlrnce = None

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if type(value) != auto else self.make_default("PrtrySts")

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = None

	@property
	def Umtchd(self):
		return self._Umtchd

	@Umtchd.setter
	def Umtchd(self, value):
		self._Umtchd = value if type(value) != auto else self.make_default("Umtchd")

	@Umtchd.deleter
	def Umtchd(self):
		del self._Umtchd
		self._Umtchd = None

	@property
	def Mtchd(self):
		return self._Mtchd

	@Mtchd.setter
	def Mtchd(self, value):
		self._Mtchd = value if type(value) != auto else self.make_default("Mtchd")

	@Mtchd.deleter
	def Mtchd(self):
		del self._Mtchd
		self._Mtchd = None

	@property
	def MtchgAllgd(self):
		return self._MtchgAllgd

	@MtchgAllgd.setter
	def MtchgAllgd(self, value):
		self._MtchgAllgd = value if type(value) != auto else self.make_default("MtchgAllgd")

	@MtchgAllgd.deleter
	def MtchgAllgd(self):
		del self._MtchgAllgd
		self._MtchgAllgd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtchdWthTlrnce', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Umtchd', type=MatchingReason6Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mtchd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtchgAllgd', type=MatchingReason5Choice, min=0, max=1, mutex_group=1, array=False),
	))

