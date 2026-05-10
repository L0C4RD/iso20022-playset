import base_types
import TrueFalseIndicator
import DateAndDateTime2Choice

class SecurityCSDLinkUpdate3(base_types._BaseFieldType):

	__slots__ = ["_VldTo", "_DfltLk"]
	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if type(value) != auto else self.make_default("VldTo")

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = None

	@property
	def DfltLk(self):
		return self._DfltLk

	@DfltLk.setter
	def DfltLk(self, value):
		self._DfltLk = value if type(value) != auto else self.make_default("DfltLk")

	@DfltLk.deleter
	def DfltLk(self):
		del self._DfltLk
		self._DfltLk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VldTo', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltLk', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

