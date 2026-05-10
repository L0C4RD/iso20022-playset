import base_types
import Max35Text
import YesNoIndicator
import InformationDistribution1Choice

class Notification2(base_types._BaseFieldType):

	__slots__ = ["_DstrbtnTp", "_NtfctnTp", "_Reqrd"]
	@property
	def DstrbtnTp(self):
		return self._DstrbtnTp

	@DstrbtnTp.setter
	def DstrbtnTp(self, value):
		self._DstrbtnTp = value if type(value) != auto else self.make_default("DstrbtnTp")

	@DstrbtnTp.deleter
	def DstrbtnTp(self):
		del self._DstrbtnTp
		self._DstrbtnTp = None

	@property
	def NtfctnTp(self):
		return self._NtfctnTp

	@NtfctnTp.setter
	def NtfctnTp(self, value):
		self._NtfctnTp = value if type(value) != auto else self.make_default("NtfctnTp")

	@NtfctnTp.deleter
	def NtfctnTp(self):
		del self._NtfctnTp
		self._NtfctnTp = None

	@property
	def Reqrd(self):
		return self._Reqrd

	@Reqrd.setter
	def Reqrd(self, value):
		self._Reqrd = value if type(value) != auto else self.make_default("Reqrd")

	@Reqrd.deleter
	def Reqrd(self):
		del self._Reqrd
		self._Reqrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DstrbtnTp', type=InformationDistribution1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnTp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reqrd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

