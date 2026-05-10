from . import base_types
from .DocumentIdentification28 import DocumentIdentification28
from .Number import Number

class DocumentEntryAmendment1(base_types._BaseFieldType):

	__slots__ = ["_OrgnlDoc", "_CrrctgNtryNb"]
	@property
	def OrgnlDoc(self):
		return self._OrgnlDoc

	@OrgnlDoc.setter
	def OrgnlDoc(self, value):
		self._OrgnlDoc = value if type(value) != base_types.auto else self.make_default("OrgnlDoc")

	@OrgnlDoc.deleter
	def OrgnlDoc(self):
		del self._OrgnlDoc
		self._OrgnlDoc = None

	@property
	def CrrctgNtryNb(self):
		return self._CrrctgNtryNb

	@CrrctgNtryNb.setter
	def CrrctgNtryNb(self, value):
		self._CrrctgNtryNb = value if type(value) != base_types.auto else self.make_default("CrrctgNtryNb")

	@CrrctgNtryNb.deleter
	def CrrctgNtryNb(self):
		del self._CrrctgNtryNb
		self._CrrctgNtryNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlDoc', type=DocumentIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrctgNtryNb', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

