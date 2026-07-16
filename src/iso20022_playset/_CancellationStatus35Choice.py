# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationProcessingStatus2
from . import PendingCancellationStatus19Choice
from . import RejectedStatus31Choice

class CancellationStatus35Choice(base_types._BaseFieldType):

	__slots__ = ["_PdgCxl", "_PrcgSts", "_Rjctd"]
	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if value is not None else base_types.UninitialisedField(self, 'PdgCxl', PendingCancellationStatus19Choice, False)

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = base_types.UninitialisedField(self, 'PdgCxl', PendingCancellationStatus19Choice, False)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', CancellationProcessingStatus2, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', CancellationProcessingStatus2, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatus31Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatus31Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgCxl', type=PendingCancellationStatus19Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrcgSts', type=CancellationProcessingStatus2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus31Choice, min=0, max=1, mutex_group=1, array=False),
	))