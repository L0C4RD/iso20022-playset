# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoReasonCode
from . import PendingCancellationStatus17Choice
from . import ProprietaryStatusAndReason6
from . import RejectedStatus62Choice

class InstructionCancellationRequestStatus20Choice(base_types._BaseFieldType):

	__slots__ = ["_CxlCmpltd", "_PdgCxl", "_PrtrySts", "_Rjctd"]
	@property
	def CxlCmpltd(self):
		return self._CxlCmpltd

	@CxlCmpltd.setter
	def CxlCmpltd(self, value):
		self._CxlCmpltd = value if value is not None else base_types.UninitialisedField(self, 'CxlCmpltd', NoReasonCode, False)

	@CxlCmpltd.deleter
	def CxlCmpltd(self):
		del self._CxlCmpltd
		self._CxlCmpltd = base_types.UninitialisedField(self, 'CxlCmpltd', NoReasonCode, False)

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if value is not None else base_types.UninitialisedField(self, 'PdgCxl', PendingCancellationStatus17Choice, False)

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = base_types.UninitialisedField(self, 'PdgCxl', PendingCancellationStatus17Choice, False)

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
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatus62Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatus62Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlCmpltd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingCancellationStatus17Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus62Choice, min=0, max=1, mutex_group=1, array=False),
	))