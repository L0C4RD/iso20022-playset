# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationStatus29Choice
from . import PendingStatus56Choice
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6
from . import RejectionStatus34Choice

class CancellationStatus30Choice(base_types._BaseFieldType):

	__slots__ = ["_Canc", "_Pdg", "_Prcd", "_Prtry", "_Rjctd"]
	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if value is not None else base_types.UninitialisedField(self, 'Canc', CancellationStatus29Choice, False)

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = base_types.UninitialisedField(self, 'Canc', CancellationStatus29Choice, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus56Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus56Choice, False)

	@property
	def Prcd(self):
		return self._Prcd

	@Prcd.setter
	def Prcd(self, value):
		self._Prcd = value if value is not None else base_types.UninitialisedField(self, 'Prcd', ProprietaryReason4, False)

	@Prcd.deleter
	def Prcd(self):
		del self._Prcd
		self._Prcd = base_types.UninitialisedField(self, 'Prcd', ProprietaryReason4, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectionStatus34Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectionStatus34Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Canc', type=CancellationStatus29Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus56Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prcd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionStatus34Choice, min=0, max=1, mutex_group=1, array=False),
	))