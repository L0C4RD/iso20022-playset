# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventType35Code
from . import ExtendedEventType8Code

class CorporateActionEventType126Choice(base_types._BaseFieldType):

	__slots__ = ["_PlainCorpEvtTp", "_XtndedCorpEvtTp"]
	@property
	def PlainCorpEvtTp(self):
		return self._PlainCorpEvtTp

	@PlainCorpEvtTp.setter
	def PlainCorpEvtTp(self, value):
		self._PlainCorpEvtTp = value if value is not None else base_types.UninitialisedField(self, 'PlainCorpEvtTp', CorporateActionEventType35Code, False)

	@PlainCorpEvtTp.deleter
	def PlainCorpEvtTp(self):
		del self._PlainCorpEvtTp
		self._PlainCorpEvtTp = base_types.UninitialisedField(self, 'PlainCorpEvtTp', CorporateActionEventType35Code, False)

	@property
	def XtndedCorpEvtTp(self):
		return self._XtndedCorpEvtTp

	@XtndedCorpEvtTp.setter
	def XtndedCorpEvtTp(self, value):
		self._XtndedCorpEvtTp = value if value is not None else base_types.UninitialisedField(self, 'XtndedCorpEvtTp', ExtendedEventType8Code, False)

	@XtndedCorpEvtTp.deleter
	def XtndedCorpEvtTp(self):
		del self._XtndedCorpEvtTp
		self._XtndedCorpEvtTp = base_types.UninitialisedField(self, 'XtndedCorpEvtTp', ExtendedEventType8Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlainCorpEvtTp', type=CorporateActionEventType35Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedCorpEvtTp', type=ExtendedEventType8Code, min=0, max=1, mutex_group=1, array=False),
	))