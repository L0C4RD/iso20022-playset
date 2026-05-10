import base_types
import NoSpecifiedReason1
import PendingStatus75Choice
import ProprietaryStatusAndReason7

class EventProcessingStatus8Choice(base_types._BaseFieldType):

	__slots__ = ["_Pdg", "_PrtrySts", "_Rcncld", "_Cmplt"]
	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

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
	def Rcncld(self):
		return self._Rcncld

	@Rcncld.setter
	def Rcncld(self, value):
		self._Rcncld = value if type(value) != auto else self.make_default("Rcncld")

	@Rcncld.deleter
	def Rcncld(self):
		del self._Rcncld
		self._Rcncld = None

	@property
	def Cmplt(self):
		return self._Cmplt

	@Cmplt.setter
	def Cmplt(self, value):
		self._Cmplt = value if type(value) != auto else self.make_default("Cmplt")

	@Cmplt.deleter
	def Cmplt(self):
		del self._Cmplt
		self._Cmplt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pdg', type=PendingStatus75Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rcncld', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmplt', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
	))

