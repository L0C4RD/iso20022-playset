# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text

class InvoiceIdentification1(base_types._BaseFieldType):

	__slots__ = ["_InvcNb", "_IsseDt"]
	@property
	def InvcNb(self):
		return self._InvcNb

	@InvcNb.setter
	def InvcNb(self, value):
		self._InvcNb = value if value is not None else base_types.UninitialisedField(self, 'InvcNb', Max35Text, False)

	@InvcNb.deleter
	def InvcNb(self):
		del self._InvcNb
		self._InvcNb = base_types.UninitialisedField(self, 'InvcNb', Max35Text, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvcNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))