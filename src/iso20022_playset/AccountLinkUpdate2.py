import base_types
import DateAndDateTime2Choice

class AccountLinkUpdate2(base_types._BaseFieldType):

	__slots__ = ["_VldTo"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='VldTo', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))

