# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClassificationType4
from . import Document28
from . import GenericIdentification175
from . import PartyIdentification260Choice
from . import SecurityIdentification49

class MetadataReport5(base_types._BaseFieldType):

	__slots__ = ["_ColltnBody", "_RgltryData", "_RgltryDataTp", "_RltdNtty", "_RltdPdctIdr", "_SubmitgNtty"]
	@property
	def ColltnBody(self):
		return self._ColltnBody

	@ColltnBody.setter
	def ColltnBody(self, value):
		self._ColltnBody = value if value is not None else base_types.UninitialisedField(self, 'ColltnBody', GenericIdentification175, False)

	@ColltnBody.deleter
	def ColltnBody(self):
		del self._ColltnBody
		self._ColltnBody = base_types.UninitialisedField(self, 'ColltnBody', GenericIdentification175, False)

	@property
	def RgltryData(self):
		return self._RgltryData

	@RgltryData.setter
	def RgltryData(self, value):
		self._RgltryData = value if value is not None else base_types.UninitialisedField(self, 'RgltryData', Document28, True)

	@RgltryData.deleter
	def RgltryData(self):
		del self._RgltryData
		self._RgltryData = base_types.UninitialisedField(self, 'RgltryData', Document28, True)

	@property
	def RgltryDataTp(self):
		return self._RgltryDataTp

	@RgltryDataTp.setter
	def RgltryDataTp(self, value):
		self._RgltryDataTp = value if value is not None else base_types.UninitialisedField(self, 'RgltryDataTp', ClassificationType4, True)

	@RgltryDataTp.deleter
	def RgltryDataTp(self):
		del self._RgltryDataTp
		self._RgltryDataTp = base_types.UninitialisedField(self, 'RgltryDataTp', ClassificationType4, True)

	@property
	def RltdNtty(self):
		return self._RltdNtty

	@RltdNtty.setter
	def RltdNtty(self, value):
		self._RltdNtty = value if value is not None else base_types.UninitialisedField(self, 'RltdNtty', PartyIdentification260Choice, True)

	@RltdNtty.deleter
	def RltdNtty(self):
		del self._RltdNtty
		self._RltdNtty = base_types.UninitialisedField(self, 'RltdNtty', PartyIdentification260Choice, True)

	@property
	def RltdPdctIdr(self):
		return self._RltdPdctIdr

	@RltdPdctIdr.setter
	def RltdPdctIdr(self, value):
		self._RltdPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'RltdPdctIdr', SecurityIdentification49, True)

	@RltdPdctIdr.deleter
	def RltdPdctIdr(self):
		del self._RltdPdctIdr
		self._RltdPdctIdr = base_types.UninitialisedField(self, 'RltdPdctIdr', SecurityIdentification49, True)

	@property
	def SubmitgNtty(self):
		return self._SubmitgNtty

	@SubmitgNtty.setter
	def SubmitgNtty(self, value):
		self._SubmitgNtty = value if value is not None else base_types.UninitialisedField(self, 'SubmitgNtty', PartyIdentification260Choice, False)

	@SubmitgNtty.deleter
	def SubmitgNtty(self):
		del self._SubmitgNtty
		self._SubmitgNtty = base_types.UninitialisedField(self, 'SubmitgNtty', PartyIdentification260Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ColltnBody', type=GenericIdentification175, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryData', type=Document28, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RgltryDataTp', type=ClassificationType4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdNtty', type=PartyIdentification260Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdPdctIdr', type=SecurityIdentification49, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgNtty', type=PartyIdentification260Choice, min=0, max=1, mutex_group=None, array=False),
	))