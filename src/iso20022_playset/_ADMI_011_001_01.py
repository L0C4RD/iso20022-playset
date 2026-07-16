# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SystemEventAcknowledgementV01

class ADMI_011_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:admi.011.001.01"
		_docname = "admi.011.001.01"

		__slots__ = ["_SysEvtAck"]
		@property
		def SysEvtAck(self):
			return self._SysEvtAck

		@SysEvtAck.setter
		def SysEvtAck(self, value):
			self._SysEvtAck = value if value is not None else base_types.UninitialisedField(self, 'SysEvtAck', SystemEventAcknowledgementV01, False)

		@SysEvtAck.deleter
		def SysEvtAck(self):
			del self._SysEvtAck
			self._SysEvtAck = base_types.UninitialisedField(self, 'SysEvtAck', SystemEventAcknowledgementV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SysEvtAck', type=SystemEventAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))