# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotificationOfCorrespondenceV01

class ADMI_024_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:admi.024.001.01"
		_docname = "admi.024.001.01"

		__slots__ = ["_NtfctnOfCrspdc"]
		@property
		def NtfctnOfCrspdc(self):
			return self._NtfctnOfCrspdc

		@NtfctnOfCrspdc.setter
		def NtfctnOfCrspdc(self, value):
			self._NtfctnOfCrspdc = value if value is not None else base_types.UninitialisedField(self, 'NtfctnOfCrspdc', NotificationOfCorrespondenceV01, False)

		@NtfctnOfCrspdc.deleter
		def NtfctnOfCrspdc(self):
			del self._NtfctnOfCrspdc
			self._NtfctnOfCrspdc = base_types.UninitialisedField(self, 'NtfctnOfCrspdc', NotificationOfCorrespondenceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnOfCrspdc', type=NotificationOfCorrespondenceV01, min=1, max=1, mutex_group=None, array=False),
		))