import base_types
import CardDataReading5Code
import Max35Text

class Vehicle2(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_NtryMd", "_Data"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def NtryMd(self):
		return self._NtryMd

	@NtryMd.setter
	def NtryMd(self, value):
		self._NtryMd = value if type(value) != auto else self.make_default("NtryMd")

	@NtryMd.deleter
	def NtryMd(self):
		del self._NtryMd
		self._NtryMd = None

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryMd', type=CardDataReading5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

