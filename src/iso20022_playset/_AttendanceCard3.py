# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeliveryPlace3Code
from . import Max105Text
from . import NameAndAddress9

class AttendanceCard3(base_types._BaseFieldType):

	__slots__ = ["_AttndncCardLbllg", "_DlvryMtd", "_OthrAdr"]
	@property
	def AttndncCardLbllg(self):
		return self._AttndncCardLbllg

	@AttndncCardLbllg.setter
	def AttndncCardLbllg(self, value):
		self._AttndncCardLbllg = value if value is not None else base_types.UninitialisedField(self, 'AttndncCardLbllg', Max105Text, False)

	@AttndncCardLbllg.deleter
	def AttndncCardLbllg(self):
		del self._AttndncCardLbllg
		self._AttndncCardLbllg = base_types.UninitialisedField(self, 'AttndncCardLbllg', Max105Text, False)

	@property
	def DlvryMtd(self):
		return self._DlvryMtd

	@DlvryMtd.setter
	def DlvryMtd(self, value):
		self._DlvryMtd = value if value is not None else base_types.UninitialisedField(self, 'DlvryMtd', DeliveryPlace3Code, False)

	@DlvryMtd.deleter
	def DlvryMtd(self):
		del self._DlvryMtd
		self._DlvryMtd = base_types.UninitialisedField(self, 'DlvryMtd', DeliveryPlace3Code, False)

	@property
	def OthrAdr(self):
		return self._OthrAdr

	@OthrAdr.setter
	def OthrAdr(self, value):
		self._OthrAdr = value if value is not None else base_types.UninitialisedField(self, 'OthrAdr', NameAndAddress9, False)

	@OthrAdr.deleter
	def OthrAdr(self):
		del self._OthrAdr
		self._OthrAdr = base_types.UninitialisedField(self, 'OthrAdr', NameAndAddress9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttndncCardLbllg', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryMtd', type=DeliveryPlace3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAdr', type=NameAndAddress9, min=0, max=1, mutex_group=None, array=False),
	))