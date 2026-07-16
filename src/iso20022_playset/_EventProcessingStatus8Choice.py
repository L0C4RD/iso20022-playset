# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoSpecifiedReason1
from . import PendingStatus75Choice
from . import ProprietaryStatusAndReason7

class EventProcessingStatus8Choice(base_types._BaseFieldType):

	__slots__ = ["_Cmplt", "_Pdg", "_PrtrySts", "_Rcncld"]
	@property
	def Cmplt(self):
		return self._Cmplt

	@Cmplt.setter
	def Cmplt(self, value):
		self._Cmplt = value if value is not None else base_types.UninitialisedField(self, 'Cmplt', NoSpecifiedReason1, False)

	@Cmplt.deleter
	def Cmplt(self):
		del self._Cmplt
		self._Cmplt = base_types.UninitialisedField(self, 'Cmplt', NoSpecifiedReason1, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus75Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus75Choice, False)

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if value is not None else base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason7, False)

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason7, False)

	@property
	def Rcncld(self):
		return self._Rcncld

	@Rcncld.setter
	def Rcncld(self, value):
		self._Rcncld = value if value is not None else base_types.UninitialisedField(self, 'Rcncld', NoSpecifiedReason1, False)

	@Rcncld.deleter
	def Rcncld(self):
		del self._Rcncld
		self._Rcncld = base_types.UninitialisedField(self, 'Rcncld', NoSpecifiedReason1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmplt', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus75Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rcncld', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
	))