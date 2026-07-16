# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import OrderStatus3Choice
from . import PartyIdentification113

class OrderStatusAndReason10(base_types._BaseFieldType):

	__slots__ = ["_MstrRef", "_OrdrSts", "_StsInitr"]
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
	def OrdrSts(self):
		return self._OrdrSts

	@OrdrSts.setter
	def OrdrSts(self, value):
		self._OrdrSts = value if value is not None else base_types.UninitialisedField(self, 'OrdrSts', OrderStatus3Choice, False)

	@OrdrSts.deleter
	def OrdrSts(self):
		del self._OrdrSts
		self._OrdrSts = base_types.UninitialisedField(self, 'OrdrSts', OrderStatus3Choice, False)

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
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrSts', type=OrderStatus3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
	))