import base_types
import PartyReport4
import ErrorHandling5

class PartyOrOperationalError4Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_PtyRpt"]
	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	@property
	def PtyRpt(self):
		return self._PtyRpt

	@PtyRpt.setter
	def PtyRpt(self, value):
		self._PtyRpt = value if type(value) != auto else self.make_default("PtyRpt")

	@PtyRpt.deleter
	def PtyRpt(self):
		del self._PtyRpt
		self._PtyRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='PtyRpt', type=PartyReport4, min=1, max=None, mutex_group=1, array=True),
	))

