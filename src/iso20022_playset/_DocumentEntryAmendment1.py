# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification28
from . import Number

class DocumentEntryAmendment1(base_types._BaseFieldType):

	__slots__ = ["_CrrctgNtryNb", "_OrgnlDoc"]
	@property
	def CrrctgNtryNb(self):
		return self._CrrctgNtryNb

	@CrrctgNtryNb.setter
	def CrrctgNtryNb(self, value):
		self._CrrctgNtryNb = value if value is not None else base_types.UninitialisedField(self, 'CrrctgNtryNb', Number, False)

	@CrrctgNtryNb.deleter
	def CrrctgNtryNb(self):
		del self._CrrctgNtryNb
		self._CrrctgNtryNb = base_types.UninitialisedField(self, 'CrrctgNtryNb', Number, False)

	@property
	def OrgnlDoc(self):
		return self._OrgnlDoc

	@OrgnlDoc.setter
	def OrgnlDoc(self, value):
		self._OrgnlDoc = value if value is not None else base_types.UninitialisedField(self, 'OrgnlDoc', DocumentIdentification28, False)

	@OrgnlDoc.deleter
	def OrgnlDoc(self):
		del self._OrgnlDoc
		self._OrgnlDoc = base_types.UninitialisedField(self, 'OrgnlDoc', DocumentIdentification28, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrrctgNtryNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDoc', type=DocumentIdentification28, min=1, max=1, mutex_group=None, array=False),
	))