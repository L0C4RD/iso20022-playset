# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelledStatus11Choice
from . import NoSpecifiedReason1
from . import PendingCancellationStatus18Choice
from . import ProprietaryStatusAndReason6
from . import RejectedStatus65Choice

class InstructionCancellationRequestStatus21Choice(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_CxlCmpltd", "_PdgCxl", "_PrtrySts", "_Rjctd"]
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
	def CxlCmpltd(self):
		return self._CxlCmpltd

	@CxlCmpltd.setter
	def CxlCmpltd(self, value):
		self._CxlCmpltd = value if value is not None else base_types.UninitialisedField(self, 'CxlCmpltd', CancelledStatus11Choice, False)

	@CxlCmpltd.deleter
	def CxlCmpltd(self):
		del self._CxlCmpltd
		self._CxlCmpltd = base_types.UninitialisedField(self, 'CxlCmpltd', CancelledStatus11Choice, False)

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if value is not None else base_types.UninitialisedField(self, 'PdgCxl', PendingCancellationStatus18Choice, False)

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = base_types.UninitialisedField(self, 'PdgCxl', PendingCancellationStatus18Choice, False)

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
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatus65Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatus65Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlCmpltd', type=CancelledStatus11Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingCancellationStatus18Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus65Choice, min=0, max=1, mutex_group=1, array=False),
	))