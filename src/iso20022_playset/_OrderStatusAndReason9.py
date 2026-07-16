# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationStatus22Choice
from . import Max35Text
from . import PartyIdentification113

class OrderStatusAndReason9(base_types._BaseFieldType):

	__slots__ = ["_CxlSts", "_MstrRef", "_StsInitr"]
	@property
	def CxlSts(self):
		return self._CxlSts

	@CxlSts.setter
	def CxlSts(self, value):
		self._CxlSts = value if value is not None else base_types.UninitialisedField(self, 'CxlSts', CancellationStatus22Choice, False)

	@CxlSts.deleter
	def CxlSts(self):
		del self._CxlSts
		self._CxlSts = base_types.UninitialisedField(self, 'CxlSts', CancellationStatus22Choice, False)

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if value is not None else base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@property
	def StsInitr(self):
		return self._StsInitr

	@StsInitr.setter
	def StsInitr(self, value):
		self._StsInitr = value if value is not None else base_types.UninitialisedField(self, 'StsInitr', PartyIdentification113, False)

	@StsInitr.deleter
	def StsInitr(self):
		del self._StsInitr
		self._StsInitr = base_types.UninitialisedField(self, 'StsInitr', PartyIdentification113, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlSts', type=CancellationStatus22Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
	))