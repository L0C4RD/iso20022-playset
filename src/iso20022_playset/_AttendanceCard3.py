from . import base_types
from ._DeliveryPlace3Code import DeliveryPlace3Code
from ._Max105Text import Max105Text
from ._NameAndAddress9 import NameAndAddress9

class AttendanceCard3(base_types._BaseFieldType):

	__slots__ = ["_AttndncCardLbllg", "_DlvryMtd", "_OthrAdr"]
	@property
	def AttndncCardLbllg(self):
		return self._AttndncCardLbllg

	@AttndncCardLbllg.setter
	def AttndncCardLbllg(self, value):
		self._AttndncCardLbllg = value if type(value) != base_types.auto else self.make_default("AttndncCardLbllg")

	@AttndncCardLbllg.deleter
	def AttndncCardLbllg(self):
		del self._AttndncCardLbllg
		self._AttndncCardLbllg = None

	@property
	def DlvryMtd(self):
		return self._DlvryMtd

	@DlvryMtd.setter
	def DlvryMtd(self, value):
		self._DlvryMtd = value if type(value) != base_types.auto else self.make_default("DlvryMtd")

	@DlvryMtd.deleter
	def DlvryMtd(self):
		del self._DlvryMtd
		self._DlvryMtd = None

	@property
	def OthrAdr(self):
		return self._OthrAdr

	@OthrAdr.setter
	def OthrAdr(self, value):
		self._OthrAdr = value if type(value) != base_types.auto else self.make_default("OthrAdr")

	@OthrAdr.deleter
	def OthrAdr(self):
		del self._OthrAdr
		self._OthrAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttndncCardLbllg', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryMtd', type=DeliveryPlace3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAdr', type=NameAndAddress9, min=0, max=1, mutex_group=None, array=False),
	))

