import base_types
import Max35Text
import ISODate

class InvoiceIdentification1(base_types._BaseFieldType):

	__slots__ = ["_IsseDt", "_InvcNb"]
	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def InvcNb(self):
		return self._InvcNb

	@InvcNb.setter
	def InvcNb(self, value):
		self._InvcNb = value if type(value) != auto else self.make_default("InvcNb")

	@InvcNb.deleter
	def InvcNb(self):
		del self._InvcNb
		self._InvcNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

