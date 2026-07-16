# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationStatus29Choice
from . import PendingStatus56Choice
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6
from . import RejectionStatus33Choice

class ProcessingStatus82Choice(base_types._BaseFieldType):

	__slots__ = ["_Canc", "_CxlReq", "_Futr", "_PdgCxl", "_Prcd", "_Prtry", "_Rjctd"]
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
	def CxlReq(self):
		return self._CxlReq

	@CxlReq.setter
	def CxlReq(self, value):
		self._CxlReq = value if value is not None else base_types.UninitialisedField(self, 'CxlReq', ProprietaryReason4, False)

	@CxlReq.deleter
	def CxlReq(self):
		del self._CxlReq
		self._CxlReq = base_types.UninitialisedField(self, 'CxlReq', ProprietaryReason4, False)

	@property
	def Futr(self):
		return self._Futr

	@Futr.setter
	def Futr(self, value):
		self._Futr = value if value is not None else base_types.UninitialisedField(self, 'Futr', ProprietaryReason4, False)

	@Futr.deleter
	def Futr(self):
		del self._Futr
		self._Futr = base_types.UninitialisedField(self, 'Futr', ProprietaryReason4, False)

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if value is not None else base_types.UninitialisedField(self, 'PdgCxl', PendingStatus56Choice, False)

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = base_types.UninitialisedField(self, 'PdgCxl', PendingStatus56Choice, False)

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
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectionStatus33Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectionStatus33Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Canc', type=CancellationStatus29Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReq', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Futr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingStatus56Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prcd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionStatus33Choice, min=0, max=1, mutex_group=1, array=False),
	))