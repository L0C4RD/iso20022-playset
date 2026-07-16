# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Number

class DocumentAmendment1(base_types._BaseFieldType):

	__slots__ = ["_CrrctnId", "_OrgnlDocId"]
	@property
	def CrrctnId(self):
		return self._CrrctnId

	@CrrctnId.setter
	def CrrctnId(self, value):
		self._CrrctnId = value if value is not None else base_types.UninitialisedField(self, 'CrrctnId', Number, False)

	@CrrctnId.deleter
	def CrrctnId(self):
		del self._CrrctnId
		self._CrrctnId = base_types.UninitialisedField(self, 'CrrctnId', Number, False)

	@property
	def OrgnlDocId(self):
		return self._OrgnlDocId

	@OrgnlDocId.setter
	def OrgnlDocId(self, value):
		self._OrgnlDocId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlDocId', Max35Text, False)

	@OrgnlDocId.deleter
	def OrgnlDocId(self):
		del self._OrgnlDocId
		self._OrgnlDocId = base_types.UninitialisedField(self, 'OrgnlDocId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrrctnId', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDocId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))