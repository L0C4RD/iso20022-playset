# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelledStatus12Choice
from . import NoSpecifiedReason1
from . import PendingCancellationStatus13Choice
from . import PendingStatus71Choice
from . import RejectedStatus58Choice
from . import ReturnedStatus2Choice

class InstructionProcessingStatus56Choice(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_AccptdForFrthrPrcg", "_Canc", "_Cvrd", "_Pdg", "_PdgCxl", "_Rjctd", "_Rtrd", "_Ucvrd"]
	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if value is not None else base_types.UninitialisedField(self, 'Accptd', NoSpecifiedReason1, False)

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = base_types.UninitialisedField(self, 'Accptd', NoSpecifiedReason1, False)

	@property
	def AccptdForFrthrPrcg(self):
		return self._AccptdForFrthrPrcg

	@AccptdForFrthrPrcg.setter
	def AccptdForFrthrPrcg(self, value):
		self._AccptdForFrthrPrcg = value if value is not None else base_types.UninitialisedField(self, 'AccptdForFrthrPrcg', NoSpecifiedReason1, False)

	@AccptdForFrthrPrcg.deleter
	def AccptdForFrthrPrcg(self):
		del self._AccptdForFrthrPrcg
		self._AccptdForFrthrPrcg = base_types.UninitialisedField(self, 'AccptdForFrthrPrcg', NoSpecifiedReason1, False)

	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if value is not None else base_types.UninitialisedField(self, 'Canc', CancelledStatus12Choice, False)

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = base_types.UninitialisedField(self, 'Canc', CancelledStatus12Choice, False)

	@property
	def Cvrd(self):
		return self._Cvrd

	@Cvrd.setter
	def Cvrd(self, value):
		self._Cvrd = value if value is not None else base_types.UninitialisedField(self, 'Cvrd', NoSpecifiedReason1, False)

	@Cvrd.deleter
	def Cvrd(self):
		del self._Cvrd
		self._Cvrd = base_types.UninitialisedField(self, 'Cvrd', NoSpecifiedReason1, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus71Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus71Choice, False)

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if value is not None else base_types.UninitialisedField(self, 'PdgCxl', PendingCancellationStatus13Choice, False)

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = base_types.UninitialisedField(self, 'PdgCxl', PendingCancellationStatus13Choice, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatus58Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatus58Choice, False)

	@property
	def Rtrd(self):
		return self._Rtrd

	@Rtrd.setter
	def Rtrd(self, value):
		self._Rtrd = value if value is not None else base_types.UninitialisedField(self, 'Rtrd', ReturnedStatus2Choice, False)

	@Rtrd.deleter
	def Rtrd(self):
		del self._Rtrd
		self._Rtrd = base_types.UninitialisedField(self, 'Rtrd', ReturnedStatus2Choice, False)

	@property
	def Ucvrd(self):
		return self._Ucvrd

	@Ucvrd.setter
	def Ucvrd(self, value):
		self._Ucvrd = value if value is not None else base_types.UninitialisedField(self, 'Ucvrd', NoSpecifiedReason1, False)

	@Ucvrd.deleter
	def Ucvrd(self):
		del self._Ucvrd
		self._Ucvrd = base_types.UninitialisedField(self, 'Ucvrd', NoSpecifiedReason1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AccptdForFrthrPrcg', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancelledStatus12Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cvrd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus71Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingCancellationStatus13Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus58Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rtrd', type=ReturnedStatus2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ucvrd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
	))